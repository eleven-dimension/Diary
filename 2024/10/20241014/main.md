甲辰年 甲戌月 辛亥日

阴有小雨

金水好旺。

国区每日难，题号 887, 越了。美区简单，一眼一发。

oi wiki 的试除法筛质数怎么溢出了，issue 启动。

看点筛法。

看魔尺海龟，突发奇想，同一个形式还有花色的区别，以前一直没注意到。

![白](JOHX{DXRHFKGF_F4JE71Z9P.jpg)

![蓝](GY_RJ{A0H43%]U$]7VFT810.jpg)

翻魔尺吧精品贴，发现好多新的样式，还有的小时候扭过但后来忘记有这种形式了，摆烂时候玩。

线筛还是没有完全领悟。操作数指点，给我看他出的题。数据范围加操作总数都是 1e5，以为必须 log，直接排除正解线段树。

线筛还是太妙了。鉴定为越短的算法越难越妙。

```cpp
vector<bool> is_prime(n + 1, true);
vector<int> primes;
is_prime[0] = is_prime[1] = false;

for (ll i = 2; i <= n; i++) {
  if (is_prime[i]) {
    primes.emplace_back(i);
  }
  for (ll j = 0; j < primes.size() && i * primes[j] <= n; j++) {
    is_prime[i * primes[j]] = false;
    if (i % primes[j] == 0) {
      break;
    }
  }
}
```

太妙了，贴一下。

老学校账户都没了，那我缺的学费这一块儿谁给我补啊，讨债启动。

操作数竟然是看到公司快倒闭主动跑路。八字看不到这么细。

找了道筛法橙题，一发过但写了好久好多。输入输出混一起了，明天整一下。操作数指点。

蒋凌宇癸未 辛酉 戊子，推测从儿，忧接下来南方火运，恐不禄。
