/* Assisted Theyyam search: header dialog on every page, plus live filtering on /theyyams/. Plain JS, no dependencies. */
(function(){
  var me=document.currentScript||document.querySelector('script[src$="search.js"]');
  var base=me.src.replace(/search\.js.*$/,'');           // .../assets/
  var root=base.replace(/assets\/$/,'');                    // site root
  var data=null,loading=null;
  function norm(s){return (s||'').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'').replace(/[^a-z0-9ഀ-ൿ ]+/g,' ').replace(/\s+/g,' ').trim();}
  function lev(a,b,max){var m=a.length,n=b.length;if(Math.abs(m-n)>max)return max+1;var p=[],i,j;for(j=0;j<=n;j++)p[j]=j;
    for(i=1;i<=m;i++){var c=[i],lo=i;for(j=1;j<=n;j++){c[j]=Math.min(p[j]+1,c[j-1]+1,p[j-1]+(a[i-1]===b[j-1]?0:1));if(c[j]<lo)lo=c[j];}if(lo>max)return max+1;p=c;}return p[n];}
  function load(){
    if(data)return Promise.resolve(data);
    if(!loading)loading=fetch(base+'theyyams.json').then(function(r){return r.json()}).then(function(d){
      d.forEach(function(e){
        e.names=[e.n].concat(e.a,[e.m]).map(norm);
        e.words=[];e.names.forEach(function(n){n.split(' ').forEach(function(w){if(w.length>2&&e.words.indexOf(w)<0)e.words.push(w)})});
        e.tg=e.g.map(norm).concat([norm(e.cl)]);
        e.tx=norm(e.t+' '+e.x);
      });data=d;return d;});
    return loading;
  }
  function scoreTok(e,q){
    var s=0,i,n;
    for(i=0;i<e.names.length;i++){n=e.names[i];
      if(n===q)s=Math.max(s,100);
      else if(n.indexOf(q)===0)s=Math.max(s,85);
      else if((' '+n).indexOf(' '+q)>-1)s=Math.max(s,72);
      else if(q.length>2&&n.indexOf(q)>-1)s=Math.max(s,55);}
    for(i=0;i<e.tg.length;i++){n=e.tg[i];
      if(n===q||n.indexOf(q)===0||(' '+n).indexOf(' '+q)>-1)s=Math.max(s,45);}
    if(q.length>2&&e.tx.indexOf(q)>-1)s=Math.max(s,22);
    return s;
  }
  function fuzzy(e,q){
    if(q.length<4)return 0;var max=q.length>6?2:1,best=9;
    e.words.forEach(function(w){var d=lev(q,w,max);if(d<best)best=d;});
    return best<=max?30-best*5:0;
  }
  function search(raw){
    var q=norm(raw);if(!q)return {list:data.slice(),fuzzy:false};
    var toks=q.split(' '),out=[],fz=false;
    data.forEach(function(e){
      var tot=0,ok=true;
      toks.forEach(function(t){var s=scoreTok(e,t);if(!s)s=0;tot+=s;if(!s)ok=false;});
      if(ok)out.push({e:e,s:tot/toks.length});
    });
    if(!out.length){
      data.forEach(function(e){var tot=0,ok=true;toks.forEach(function(t){var s=Math.max(scoreTok(e,t),fuzzy(e,t));tot+=s;if(!s)ok=false;});if(ok){out.push({e:e,s:tot/toks.length});fz=true;}});
    }
    out.sort(function(a,b){return b.s-a.s||a.e.n.localeCompare(b.e.n)});
    return {list:out.map(function(o){return o.e}),fuzzy:fz};
  }
  window.TheyyamSearch={load:load,search:search,norm:norm};

  /* ---------- header dialog ---------- */
  var css='.hd .lg,.hd .nv a{white-space:nowrap}@media(min-width:768px) and (max-width:1000px){.hd .nv{gap:18px}.hd .nv a{font-size:15px}}.sbtn{display:inline-flex;align-items:center;justify-content:center;width:44px;height:44px;border-radius:999px;border:2px solid #1a0a08;background:#fff;color:#1a0a08;cursor:pointer;padding:0;flex:none}.sbtn:hover{background:#FFB400;border-color:#FFB400}.sbtn svg{pointer-events:none}'
  +'.sbtn.m{margin-left:auto;margin-right:10px}.hd .w .lg{margin-right:0}'
  +'@media(min-width:768px){.sbtn.m{display:none}}'
  +'#tsd{border:0;padding:0;margin:0;width:100%;max-width:100%;max-height:100%;height:100%;background:rgba(26,10,8,.6);color:#1a0a08;font-family:inherit}'
  +'#tsd::backdrop{background:rgba(26,10,8,.6)}'
  +'#tsd .box{background:#fff;max-width:680px;margin:0 auto;border-radius:0 0 28px 28px;padding:16px 16px 20px;max-height:92vh;display:flex;flex-direction:column}'
  +'@media(min-width:768px){#tsd .box{margin-top:48px;border-radius:28px;padding:24px}}'
  +'#tsd .row{display:flex;gap:10px;align-items:center}'
  +'#tsd input{flex:1;min-height:52px;border:2px solid #1a0a08;border-radius:999px;padding:0 20px;font:inherit;font-size:16px;color:#1a0a08;background:#fff;min-width:0}'
  +'#tsd input:focus{outline:4px solid #FFB400}'
  +'#tsd .x{min-height:44px;padding:0 14px;border:0;background:none;font:inherit;font-weight:600;cursor:pointer;color:#1a0a08}'
  +'#tsd ul{list-style:none;margin:12px 0 0;padding:0;overflow:auto}'
  +'#tsd li a{display:flex;gap:14px;align-items:center;padding:10px;border-radius:18px;text-decoration:none;color:#1a0a08}'
  +'#tsd li a:hover,#tsd li a[aria-selected=true]{background:#FFF1CC}'
  +'#tsd li img{width:56px;height:56px;border-radius:14px;object-fit:cover;flex:none;background:#eee}'
  +'#tsd li b{display:block}#tsd li small{display:block;opacity:.75;line-height:1.35}'
  +'#tsd .hint{font-size:13px;opacity:.8;margin:10px 4px 0}#tsd mark{background:#FFB400;color:inherit;border-radius:3px}'
  +'#tsd .sug{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0 0}#tsd .sug button{font:inherit;font-size:14px;min-height:40px;padding:0 14px;border:2px solid #1a0a08;border-radius:999px;background:#fff;cursor:pointer;color:#1a0a08}#tsd .sug button:hover{background:#FFB400;border-color:#FFB400}';
  var ST=document.createElement('style');ST.textContent=css;document.head.appendChild(ST);
  var icon='<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg>';
  function mk(cls){var b=document.createElement('button');b.type='button';b.className='sbtn '+(cls||'');b.setAttribute('aria-label','Search Theyyams');b.setAttribute('aria-haspopup','dialog');b.innerHTML=icon;b.addEventListener('click',open);return b;}
  var nv=document.querySelector('.hd .nv'),mm=document.querySelector('.hd .mm');
  if(nv){var enq=nv.querySelector('a.btn');var d=mk('');nv.insertBefore(d,enq);}
  if(mm){mm.parentNode.insertBefore(mk('m'),mm);}
  var dlg,inp,list,hint,sel=-1,items=[];
  function build(){
    if(dlg)return;
    dlg=document.createElement('dialog');dlg.id='tsd';dlg.setAttribute('aria-label','Search Theyyams');
    dlg.innerHTML='<div class="box"><div class="row"><input id="tsq" type="search" role="combobox" aria-expanded="true" aria-controls="tsl" aria-autocomplete="list" placeholder="Search Theyyams: name, meaning or Malayalam" autocomplete="off"><button class="x" type="button">Close</button></div><div class="hint" id="tsh" aria-live="polite"></div><div class="sug" id="tss"></div><ul id="tsl" role="listbox" aria-label="Results"></ul></div>';
    document.body.appendChild(dlg);
    inp=dlg.querySelector('#tsq');list=dlg.querySelector('#tsl');hint=dlg.querySelector('#tsh');
    dlg.querySelector('.x').addEventListener('click',function(){dlg.close()});
    dlg.addEventListener('click',function(e){if(e.target===dlg)dlg.close()});
    inp.addEventListener('input',render);
    inp.addEventListener('keydown',function(e){
      if(e.key==='ArrowDown'){e.preventDefault();move(1)}else if(e.key==='ArrowUp'){e.preventDefault();move(-1)}
      else if(e.key==='Enter'){var a=items[sel>=0?sel:0];if(a){e.preventDefault();location.href=a.href}}
    });
  }
  function move(d){if(!items.length)return;sel=(sel+d+items.length)%items.length;items.forEach(function(a,i){a.setAttribute('aria-selected',i===sel?'true':'false')});inp.setAttribute('aria-activedescendant',items[sel].id);items[sel].scrollIntoView({block:'nearest'});}
  function esc(s){return s.replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
  function hl(s,q){if(!q)return esc(s);var i=s.toLowerCase().indexOf(q.toLowerCase());if(i<0)return esc(s);return esc(s.slice(0,i))+'<mark>'+esc(s.slice(i,i+q.length))+'</mark>'+esc(s.slice(i+q.length));}
  function render(){
    load().then(function(){
      var raw=inp.value.trim(),r=search(raw),sug=dlg.querySelector('#tss');
      var shown=r.list.slice(0,8);
      list.innerHTML=shown.map(function(e,i){return '<li role="presentation"><a role="option" id="tso'+i+'" aria-selected="false" href="'+root+'theyyams/'+e.s+'.html">'+(e.f?'<img src="'+base+'theyyam/'+e.f+'" alt="" loading="lazy" width="56" height="56">':'<span style="width:56px;height:56px;border-radius:14px;background:#4A0E12;flex:none"></span>')+'<span><b>'+hl(e.n,raw)+' <span lang="ml" style="font-weight:400;opacity:.8">'+esc(e.m)+'</span></b><small>'+esc(e.cl)+' · '+esc(e.t)+'</small></span></a></li>'}).join('');
      items=[].slice.call(list.querySelectorAll('a'));sel=-1;
      if(!raw){hint.textContent='Popular: start typing, or pick one.';sug.innerHTML=['Muthappan','Vishnumoorthi','Pottan','Goddess','Hero','Harmony'].map(function(w){return '<button type="button">'+w+'</button>'}).join('');}
      else{sug.innerHTML='';hint.textContent=shown.length?(r.fuzzy?'Closest matches for “'+raw+'”':r.list.length+' Theyyam'+(r.list.length>1?'s':'')+' found'):'No match for “'+raw+'”. Try a name, “goddess”, “hero” or “harmony”.';}
      if(!shown.length&&raw)list.innerHTML='<li style="padding:10px 6px"><a href="'+root+'theyyams/">Browse all Theyyams</a></li>';
      else if(r.list.length>8)list.insertAdjacentHTML('beforeend','<li role="presentation"><a href="'+root+'theyyams/">See all '+r.list.length+' in the guide</a></li>');
      sug.querySelectorAll('button').forEach(function(b){b.addEventListener('click',function(){inp.value=b.textContent;render();inp.focus()})});
    });
  }
  function open(){build();if(!dlg.open)dlg.showModal();inp.value='';render();setTimeout(function(){inp.focus()},30);}
  document.addEventListener('keydown',function(e){if(e.key==='/'&&!/input|textarea|select/i.test((document.activeElement||{}).tagName||'')&&!(dlg&&dlg.open)){e.preventDefault();open();}});

  /* ---------- hub page filter ---------- */
  var grid=document.getElementById('hubgrid'),q=document.getElementById('hubq');
  if(grid&&q){
    var chips=[].slice.call(document.querySelectorAll('.fchips button')),cat='',status=document.getElementById('hubstatus'),empty=document.getElementById('hubempty'),dym=document.getElementById('hubdym');
    function apply(){
      load().then(function(){
        var r=search(q.value),keep={};r.list.forEach(function(e){keep[e.s]=1});
        var n=0;
        [].forEach.call(grid.querySelectorAll('.tc'),function(a){var ok=keep[a.getAttribute('data-s')]&&(!cat||a.parentNode.parentNode.getAttribute('data-c')===cat);a.style.display=ok?'':'none';if(ok)n++;});
        [].forEach.call(grid.querySelectorAll('.cg'),function(s){var any=[].some.call(s.querySelectorAll('.tc'),function(a){return a.style.display!=='none'});s.style.display=any?'':'none';});
        empty.hidden=n>0;
        var v=q.value.trim();
        status.textContent=v||cat?(n+' Theyyam'+(n===1?'':'s')+(v?' for “'+v+'”':'')+(r.fuzzy&&n?' (closest matches)':'')):'';
        if(!n){var s=search(v.replace(/\s+/g,' ')).list;dym.textContent='Try “Muthappan”, “Pottan” or “goddess”.';}
      });
    }
    q.addEventListener('input',apply);
    chips.forEach(function(b){b.addEventListener('click',function(){cat=b.getAttribute('data-c');chips.forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')});apply();});});
    var m=location.search.match(/[?&]q=([^&]*)/);if(m){q.value=decodeURIComponent(m[1].replace(/\+/g,' '));apply();}
    if(location.hash&&location.hash.length>1){var c=location.hash.slice(1);chips.forEach(function(b){if(b.getAttribute('data-c')===c)b.click()});}
  }
})();
