// in-memory fake of GitHub contents API used by the Worker
export function makeFakeGitHub(){
  const files = new Map(); let shaCounter = 0; const log = [];
  const b64 = s=>Buffer.from(s,'utf8').toString('base64');
  const un = s=>Buffer.from(s,'base64').toString('utf8');
  let failNext = null;   // {status} to inject one failure
  async function handle(url, init={}){
    const m = url.match(/\/contents\/(.+)$/); const path = decodeURIComponent(m[1]);
    const method = (init.method||'GET').toUpperCase();
    if(failNext){ const f=failNext; failNext=null; log.push([method,path,'INJECT',f.status]); return new Response('{}',{status:f.status}); }
    if(method==='GET'){
      if(!files.has(path)){ log.push(['GET',path,404]); return new Response('{"message":"Not Found"}',{status:404}); }
      const f=files.get(path); log.push(['GET',path,200]);
      return new Response(JSON.stringify({sha:f.sha,content:b64(f.text)}),{status:200});
    }
    if(method==='PUT'){
      const body=JSON.parse(init.body); const exists=files.has(path);
      if(exists && !body.sha){ log.push(['PUT',path,422]); return new Response('{"message":"sha missing"}',{status:422}); }
      if(exists && body.sha!==files.get(path).sha){ log.push(['PUT',path,409]); return new Response('{"message":"conflict"}',{status:409}); }
      const sha='sha'+(++shaCounter); files.set(path,{sha,text:un(body.content)});
      log.push(['PUT',path,exists?200:201]);
      return new Response(JSON.stringify({content:{sha}}),{status:exists?200:201});
    }
    return new Response('{}',{status:405});
  }
  return { handle, files, log, injectFail:(status)=>{failNext={status};}, read:(p)=>files.has(p)?JSON.parse(files.get(p).text):null };
}
