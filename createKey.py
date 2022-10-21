
def powMod(a, b, m):
	x = []
	while b != 0:
		x.append(b & 1)
		b = b >> 1
	sz = len(x)
	po = [a%m]
	for i in range(1,sz):
		p = (po[i-1]*po[i-1])%m
		po.append(p)
	r = 1
	for i in range(sz):
		if(x[i] != 0):
			r*= po[i]
			r%= m
	return r

def GCD(a, b):
	if b == 0:
		return a
	return GCD(b, a%b)

# a*x + b*y = z
def GCD_extended(a, b):
	u1, u2, u3 = 1, 0, a
	v1, v2, v3 = 0, 1, b
	while v3 != 0:
		q = u3//v3
		t1, t2, t3 = u1 - q*v1, u2 - q*v2, u3 - q*v3
		u1, u2, u3 = v1, v2, v3
		v1, v2, v3 = t1, t2, t3
	return u1, u2, u3


# a = pow(201,1024)
# b = pow(301,1024)
# m = pow(951,1024)
# print(pow(a,b,m))
# print(powMod(a,b,m))

def getPQ(file):
	fi = open(file,"r")
	p = int(fi.readline())
	q = int(fi.readline())
	return p, q

def getE(phi):
	e = 65537
	while True:
		if GCD(e,phi) == 1:
			break
		e+= 2
	return e

def getD(e, phi):
	d = GCD_extended(e,phi)[0] #[x,y,z] #d = x
	if d < 0:
		d+= phi
	return d

def main():
	p, q = getPQ("D:\PYTHON\RSA\Data\BigPrime.txt")
	n = p*q
	phi = (p-1)*(q-1)
	e = getE(phi)
	d = getD(e, phi)
	fo = open("D:\PYTHON\RSA\Data\PublicKey.txt","w")
	fo.write(str(n)+'\n'+str(e))
	fo.close()
	fo = open("D:\PYTHON\RSA\Data\PrivateKey.txt","w")
	fo.write(str(n)+'\n'+str(d))
	fo.close()

main()