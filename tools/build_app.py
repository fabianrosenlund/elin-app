import sys,json
from PIL import Image
import os; R=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); src=R+'/src/elin.html'; out=R+'/site/'
url=sys.argv[1] if len(sys.argv)>1 else ''; key=sys.argv[2] if len(sys.argv)>2 else ''
s=open(src,encoding='utf-8').read()
assert s.count("const ESTIMATE_URL='', ESTIMATE_KEY='';")==1
s=s.replace("const ESTIMATE_URL='', ESTIMATE_KEY='';",f"const ESTIMATE_URL={json.dumps(url)}, ESTIMATE_KEY={json.dumps(key)};")
s=s.replace('<meta name="claude:viewport-fit-sides" content="cover">\n','')
head='''<!doctype html>
<html lang="sv">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#F3F4EC" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#1C231E" media="(prefers-color-scheme: dark)">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="ELIN">
<meta name="description" content="ELIN, ett steg i taget. Ett stöd för att logga mat och mående. Inte vård.">
<link rel="apple-touch-icon" href="icon-180.png">
<link rel="icon" type="image/png" href="icon-192.png">
<link rel="manifest" href="manifest.webmanifest">
'''
i=s.index('<title>'); j=s.index('<style>')
s=head+s[i:j]+'</head>\n<body>\n'+s[j:]
s=s.replace('</style>','</style>',1)
# style is inside body now; move style into head for correctness
a=s.index('<style>'); b=s.index('</style>')+8; style=s[a:b]; s=s[:a]+s[b:]
s=s.replace('</head>',style+'\n</head>',1)
s+='''
<script>if('serviceWorker' in navigator&&location.protocol==='https:')addEventListener('load',()=>navigator.serviceWorker.register('sw.js').catch(()=>{}));</script>
</body>
</html>
'''
open(out+'index.html','w',encoding='utf-8').write(s)
json.dump({"name":"ELIN","short_name":"ELIN","description":"Ett steg i taget. Stöd för att logga mat och mående. Inte vård.","lang":"sv","start_url":"./","scope":"./","display":"standalone","orientation":"portrait","background_color":"#F3F4EC","theme_color":"#F3F4EC",
 "icons":[{"src":"icon-192.png","sizes":"192x192","type":"image/png"},{"src":"icon-512.png","sizes":"512x512","type":"image/png"},{"src":"icon-512.png","sizes":"512x512","type":"image/png","purpose":"maskable"}]},open(out+'manifest.webmanifest','w',encoding='utf-8'),ensure_ascii=False,indent=1)
im=Image.open(R+'/assets/elin-appikon-1024.png').convert('RGB')
for n in (180,192,512): im.resize((n,n),Image.LANCZOS).save(out+f'icon-{n}.png')
open(out+'sw.js','w').write('''const C='elin-v1';const SHELL=['./','index.html','manifest.webmanifest','icon-192.png','icon-512.png','icon-180.png'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(C).then(c=>c.addAll(SHELL)).then(()=>self.skipWaiting()))});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==C).map(x=>caches.delete(x)))).then(()=>self.clients.claim()))});
self.addEventListener('fetch',e=>{const r=e.request;if(r.method!=='GET')return;const u=new URL(r.url);
  if(u.hostname.endsWith('supabase.co'))return;
  e.respondWith(fetch(r).then(res=>{if(res.ok&&(u.origin===location.origin||/fonts\\.(googleapis|gstatic)\\.com|cdnjs\\.cloudflare\\.com/.test(u.hostname))){const cp=res.clone();caches.open(C).then(c=>c.put(r,cp))}return res}).catch(()=>caches.match(r).then(m=>m||caches.match('index.html'))))});
''')
print('built', 'with AI' if url else 'without AI')
