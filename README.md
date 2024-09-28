# RSA
# RSA加密算法是一种非对称加密算法。RSA是1977年由罗纳德·李维斯特（Ron Rivest）、阿迪·萨莫尔（Adi Shamir）和伦纳德·阿德曼（Leonard Adleman）一起提出的。当时他们三人都在麻省理工学院工作。RSA就是他们三人姓氏开头字母拼在一起组成的。
# RSA的基本思想为对一整数做因式分解的难度决定了其破译的难度，只要其钥匙的长度足够长，用RSA加密的信息实际上是不能被破解的。
# RSA的基本过程如下：
1.任意选择两个大的素数p和q，要求p不等于q.同时计算出N = p * q
2.通过欧拉函数计算r
r = φ(N) = φ(p)φ(q) = (p-1)(q-1)
3.选择一个大于1小于r并且与r互质的元素e（随机选择）,满足 gcd(r,e) = 1
4.计算d，其满足：
 e * d ≡ 1 mod r ,即e和d的乘积模r的余数等于1，这里由于e与r是互素的，由模运算可知，它的乘法逆元一定存在。
5.最后将计算所得的N e d 三个，以{e,n}为公开密钥，{d,n}为私钥进行非对称的加密通信即可


