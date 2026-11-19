const $=(s,r=document)=>r.querySelector(s);
const $$=(s,r=document)=>[...r.querySelectorAll(s)];
const reduceMotion=matchMedia('(prefers-reduced-motion: reduce)');
let motionPaused=reduceMotion.matches;
const chapters=$$('[data-chapter]');
const stops=$$('[data-stop]');
const road=$('#road');
const roadLength=road.getTotalLength();
const vbw=1750;const centers=[214,539,869,1198,1566];
let positions=[];
function computePositions(){positions=centers.map(x=>{let lo=0,hi=1;for(let i=0;i<24;i++){const mid=(lo+hi)/2;if(road.getPointAtLength(roadLength*mid).x<x)lo=mid;else hi=mid;}return lo;});}
computePositions();
const thoughts=['Curiosity','Consumer insight','CTR · AOP · ROAS','Build · Test · Learn','GMV · Margin · Sell-through'];
const buildingIds=['school','college','phonepe','masters','biba'];
let activeStop=-1;
let walkPosition=positions[0];
let inCar=false;
let walkTarget=positions[0];
let navigationLockUntil=0;
let sceneVisible=true;
let frameTime=0;
function paintWalker(){
 const p=road.getPointAtLength(roadLength*walkPosition);
 inCar=walkPosition>(positions[3]+positions[4])/2;
 $('#car').style.display=inCar?'':'none';
 $('#girlSprite').style.display=inCar?'none':'';
 $('#walker').setAttribute('transform',`translate(${p.x} ${p.y-3})`);
 $('#thoughtBubble').setAttribute('transform',`translate(${Math.max(30,Math.min(vbw-175,p.x+(inCar?-20:24)))} ${p.y-(inCar?160:127)})`);
}
function setStop(i){
 if(i===activeStop)return;
 activeStop=i;walkTarget=positions[i];
 stops.forEach((s,n)=>{s.classList.toggle('active',i===n);if(i===n)s.setAttribute('aria-current','step');else s.removeAttribute('aria-current');});
 buildingIds.forEach((name,n)=>$('#building-'+name).classList.toggle('active',i===n));
 $('#thoughtText').textContent=thoughts[i];
 if(innerWidth<=1000){const w=$('#world').getBoundingClientRect().width;const cw=$('#world').parentElement.clientWidth;const lim=Math.max(0,(w-cw)/2);const s=Math.max(-lim,Math.min(lim,(vbw/2-centers[i])*w/vbw));$('#world').style.transform=`translateX(${s}px)`;}else $('#world').style.transform='';
 if(motionPaused){walkPosition=walkTarget;paintWalker();}
}
function updateChapter(){
 if(Date.now()<navigationLockUntil)return;
 const stageBottom=$('#journeyStage').getBoundingClientRect().bottom;
 let selected=0;
 for(let i=0;i<chapters.length;i++)if(chapters[i].getBoundingClientRect().top<=stageBottom+85)selected=i;
 setStop(selected);
}
function animate(t){
 if(t-frameTime>24){
  const distance=walkTarget-walkPosition;
  if(Math.abs(distance)>.0002){walkPosition=motionPaused?walkTarget:walkPosition+distance*.105;paintWalker();$('#walker').classList.toggle('walking',!motionPaused&&sceneVisible);}
  else{$('#walker').classList.remove('walking');}
  frameTime=t;
 }
 requestAnimationFrame(animate);
}
function updateMotion(){document.body.classList.toggle('motion-paused',motionPaused);$('#motionToggle').setAttribute('aria-pressed',String(motionPaused));$('#motionToggle').textContent=motionPaused?'Resume motion ▷':'Pause motion Ⅱ';if(motionPaused){walkPosition=walkTarget;paintWalker();}}
$('#motionToggle').addEventListener('click',()=>{motionPaused=!motionPaused;updateMotion();});
reduceMotion.addEventListener('change',e=>{motionPaused=e.matches;updateMotion();});
// Stop selection follows the chapter being read below the stable scene.
stops.forEach(a=>a.addEventListener('click',()=>{navigationLockUntil=Date.now()+900;setStop(Number(a.dataset.stop));setTimeout(updateChapter,950);}));
addEventListener('scroll',updateChapter,{passive:true});
addEventListener('resize',()=>{const i=activeStop;activeStop=-1;setStop(i<0?0:i);updateChapter();});
new IntersectionObserver(entries=>{sceneVisible=entries[0].isIntersecting;},{threshold:0}).observe($('#journey'));
// Pause a recording when it is off screen or another recording starts.
const videos=$$('video');
videos.forEach(v=>v.addEventListener('play',()=>videos.forEach(other=>{if(other!==v)other.pause();})));
const videoObserver=new IntersectionObserver(entries=>entries.forEach(e=>{if(!e.isIntersecting)e.target.pause();}),{threshold:0});
videos.forEach(v=>videoObserver.observe(v));
setStop(0);paintWalker();updateMotion();requestAnimationFrame(animate);updateChapter();
addEventListener('load',updateChapter);
const mediaDialog=$('#mediaDialog');let mediaOpener;
document.addEventListener('click',e=>{
 const button=e.target.closest('[data-image]');
 if(!button)return;
 mediaOpener=button;
 $('#largeImage').src=button.dataset.image;$('#largeImage').alt=button.dataset.caption;
 $('#mediaTitle').textContent=button.dataset.caption;
 mediaDialog.showModal();document.body.classList.add('modal-open');$('#closeMedia').focus();
});
$('#closeMedia').addEventListener('click',()=>mediaDialog.close());
mediaDialog.addEventListener('close',()=>{document.body.classList.remove('modal-open');mediaOpener?.focus();});
mediaDialog.addEventListener('click',e=>{if(e.target!==mediaDialog)return;const b=mediaDialog.getBoundingClientRect();if(e.clientX<b.left||e.clientX>b.right||e.clientY<b.top||e.clientY>b.bottom)mediaDialog.close();});
const rounds=[
 {title:'A sale is five days out on Myntra.',brief:'A big sale event is coming. You can fund deeper discounts and extra visibility, but not for the whole catalogue. Where does it go?',choices:[['Discount the whole catalogue evenly','It looks generous, but thin coverage on every style means none of them wins visibility, and margin drops on styles that would have sold anyway.'],['Back hero styles with full size depth','Pick the styles with proven conversion and enough stock across sizes, fund visibility and offers on them, and keep fresh styles ready to replace them as they sell out.'],['Push the slow movers hardest','Clearing old stock matters, but a sale is the best traffic of the season. Leading with your weakest styles wastes it.']],takeaway:'Back the styles you can actually ship.'},
 {title:'A kurta set is a hit. Sizes M and L are running out.',brief:'It is your top seller on Ajio this week, ads are running, and the core sizes will run out in four days. What do you do?',choices:[['Keep the ads running at full spend','You pay for traffic that lands on a broken size range. Shoppers bounce, conversion falls, and the listing loses rank just as it peaked.'],['Rebalance stock, redirect the spend','Work with supply chain to move stock in from slower channels or speed up a reorder. Meanwhile, move ad spend to similar styles with full sizes so the demand is not wasted.'],['Raise the price to slow sales down','It protects stock for now, but it chips away at conversion and rank on your best style, and it does not solve next week’s demand.']],takeaway:'Ads can’t sell what isn’t in stock.'},
 {title:'A platform asks for an extra 10% off.',brief:'Amazon wants BIBA to fund an extra 10% discount to feature it in a festive deal. Revenue would jump. What’s your answer?',choices:[['Say yes, the visibility is worth it','The spike in revenue can hide that every order now earns less, or even loses money once returns and fees come in.'],['Model the margin, then counter','Work out contribution after the discount, fees and returns with finance. Offer the deal on selected styles or a bundle where the numbers still work, and agree the visibility you get in return.'],['Decline, and protect the price','Margin stays safe, but you lose a top slot in the busiest week of the season, and the relationship with the platform team takes a hit.']],takeaway:'Grow revenue without giving away margin.'}
];
let round=0;let gameChoices=[];
function renderGame(){
 $('#gameProgress').textContent=round<3?`0${round+1} / 03`:'COMPLETE';
 if(round===3){$('#gameContent').innerHTML=`<h3>A good instinct.<br>An even better question.</h3><p>Your route through the lab: ${gameChoices.map(i=>String.fromCharCode(65+i)).join(' → ')}. Each choice opened a different trade-off.</p><div class="game-feedback"><strong>The thread through it all</strong><p>Back the styles that sell and can ship. Keep sizes in stock before you buy traffic. Negotiate for visibility, but protect the margin.</p></div><p style="margin-top:17px">That’s the kind of work I want to keep doing.</p><a href="#contact" class="text-link">Let’s plan the next test <span>↗</span></a>`;return;}
 const q=rounds[round];$('#gameContent').innerHTML=`<h3>${q.title}</h3><p>${q.brief}</p><div class="game-options">${q.choices.map((c,i)=>`<button class="game-option" data-choice="${i}"><span>${String.fromCharCode(65+i)}</span>${c[0]}<b>↗</b></button>`).join('')}</div><div id="feedback" aria-live="polite"></div>`;
}
$('#gameContent').addEventListener('click',e=>{const option=e.target.closest('[data-choice]');if(option){const i=Number(option.dataset.choice);gameChoices[round]=i;$$('.game-option').forEach(b=>b.disabled=true);option.style.background='#F5ECE0';$('#feedback').innerHTML=`<div class="game-feedback"><strong>${rounds[round].takeaway}</strong><p>${rounds[round].choices[i][1]}</p></div><button class="game-next" id="nextRound">${round===2?'Finish the experiment':'Next decision'} →</button>`;}if(e.target.closest('#nextRound')){round++;renderGame();}});
$('#resetGame').addEventListener('click',()=>{round=0;gameChoices=[];renderGame();});
renderGame();

// Opening: "Hi BIBA, I’m Ishani."
(function(){
 const screen=$('#introScreen');if(!screen)return;
 document.body.classList.add('intro-open');
 const hi=$('#typeHi'),me=$('#typeMe'),cH=$('#caretHi'),cM=$('#caretMe'),role=$('#introRole'),go=$('#introGo');
 let done=false,timers=[];
 const later=(fn,ms)=>timers.push(setTimeout(fn,ms));
 function finish(){
  if(done)return;done=true;timers.forEach(clearTimeout);
  screen.classList.add('leaving');document.body.classList.remove('intro-open');
  setTimeout(()=>screen.classList.add('gone'),650);
 }
 function type(el,text,speed,cb){let i=0;(function step(){el.innerHTML=text.slice(0,i);if(i++<text.length)later(step,speed);else cb&&cb();})();}
 const fast=reduceMotion.matches;
 if(fast){hi.textContent='Hi BIBA,';me.innerHTML='I’m <b>Ishani.</b>';role.classList.add('show');go.classList.add('show');later(finish,1200);}
 else{
  cH.classList.add('on');
  later(()=>type(hi,'Hi BIBA,',75,()=>{cH.classList.remove('on');cM.classList.add('on');
   later(()=>type(me,'I’m <b>Ishani.</b>'.replace('<b>Ishani.</b>','Ishani.'),80,()=>{
    me.innerHTML='I’m <b>Ishani.</b>';cM.classList.remove('on');
    later(()=>role.classList.add('show'),250);later(()=>go.classList.add('show'),600);later(finish,3200);
   }),250);
  }),500);
 }
 go.addEventListener('click',finish);$('#introSkip').addEventListener('click',finish);
 addEventListener('keydown',e=>{if(e.key==='Escape'||e.key==='Enter')finish();});
})();
