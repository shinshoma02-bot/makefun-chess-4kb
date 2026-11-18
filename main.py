import json,os,urllib.request as U
N,E,S,W=-10,1,10,-1
D={'P':(N,N+N,N+W,N+E),'N':(N+N+E,E+N+E,E+S+E,S+S+E,S+S+W,W+S+W,W+N+W,N+N+W),'B':(N+E,S+E,S+W,N+W),'R':(N,E,S,W)}
D['Q']=D['K']=D['B']+D['R']
V=dict(P=100,N=320,B=330,R=500,Q=900,K=0)
M=30000
Z={}
H=set()
L=40000
T={'.':[0]*120,' ':[0]*120}
for u in V:
 t=[]
 for i in range(120):
  r=i//10-2;c=i%10-1;d=min(r,7-r)+min(c,7-c)
  t+=[V[u]+((7-r)*5+d*3 if u=='P' else d*{'N':10,'B':5,'Q':2,'K':-6}.get(u,0))]
 T[u]=t;T[u.lower()]=[-t[119-i]for i in range(120)]
def ev(b):
 return sum(T[q][i]for i,q in enumerate(b))
def gen(b):
 for i,q in enumerate(b):
  if q<'A'or q>'Z':continue
  for d in D[q]:
   j=i+d
   while 1:
    t=b[j]
    if t==' 'or'A'<=t<='Z':break
    if q=='P':
     if d in(N,N+N)and t!='.':break
     if d==N+N and(i<81 or b[i+N]!='.'):break
     if d in(N+E,N+W)and t=='.':break
    yield i,j
    if q in'PNK'or t!='.':break
    j+=d
def mk(b,i,j):
 q=b[i]
 if q=='P'and j<30:q='Q'
 l=list(b);l[j]=q;l[i]='.'
 return''.join(l)[::-1].swapcase()
class X(Exception):0
def srch(b,d,a,c):
 global n
 n+=1
 if n>L:raise X
 o=a;m=0;best=-M*2
 if d>0:
  e=Z.get(b)
  if e:
   m=e[3]
   if e[0]>=d and(e[1]==0 or e[1]==1 and e[2]>=c or e[1]==2 and e[2]<=a):return e[2]
  if d>2 and c<M//2:
   s=-srch(b[::-1].swapcase(),d-3,-c,1-c)
   if s>=c:return s
 else:
  best=ev(b)
  if best>=c:return best
  a=max(a,best)
 ms=list(gen(b))
 if d<=0:ms=[x for x in ms if b[x[1]]!='.']
 ms.sort(key=lambda x:-((b[x[1]]=='k')*99999+(x==m)*9999+V.get(b[x[1]].upper(),0)*10-V[b[x[0]]]))
 bm=0
 for i,j in ms:
  if b[j]=='k':return M+d
  s=-srch(mk(b,i,j),d-1,-c,-a)
  if s>best:
   best=s;bm=i,j
   if s>a:
    a=s
    if a>=c:break
 if d>0:
  if best<-M//2:
   r=b[::-1].swapcase()
   if not any(r[j]=='k'for i,j in gen(r)):best=0
  Z[b]=d,0 if o<best<c else 1 if best>=c else 2,best,bm
 return best
def sq(k,f):
 if f:k=119-k
 return'abcdefgh'[k%10-1]+str(10-k//10+(0))
def uci(b,i,j,f):
 return sq(i,f)+sq(j,f)+('q'if b[i]=='P'and j<30 else'')
def pick(b,legal,f):
 global n
 n=0
 ms=[m for m in gen(b)if uci(b,m[0],m[1],f)in legal]
 res=ms[0]
 for d in range(1,30):
  sc=[]
  try:
   a=-M*2
   for i,j in ms:
    k=mk(b,i,j);s=-srch(k,d-1,-M*2,-a)
    if k in H and s>0:s=0
    sc.append((s,(i,j)))
    a=max(a,s)
  except X:break
  sc.sort(key=lambda x:-x[0])
  ms=[m for s,m in sc]
  res=ms[0]
  if sc[0][0]>M//2:break
 H.add(mk(b,*res))
 return uci(b,res[0],res[1],f)
def post(p,x):
 r=U.Request(os.environ['MAKEFUN_ENV_URL']+p,json.dumps(x).encode(),{'content-type':'application/json'})
 return json.load(U.urlopen(r))
def parse(fen):
 f=fen.split()
 b=' '*20
 for row in f[0].split('/'):
  b+=' '
  for ch in row:b+='.'*int(ch)if ch.isdigit()else ch
  b+=' '
 b+=' '*20
 return b,f[1]=='b'
while 1:
 g=post('/game',{})
 if g['status']=='done':break
 while g['status']=='your_move':
  b,f=parse(g['fen'])
  if f:b=b[::-1].swapcase()
  g=post('/move',{'game':g['game'],'move':pick(b,g['legal_moves'],f)})
