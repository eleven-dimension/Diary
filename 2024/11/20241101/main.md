甲辰年 甲戌月 己巳日

阴有雨

两区ez.

[难](https://leetcode.cn/problems/total-characters-in-string-after-transformations-ii/)

[写不动，下次再来吧家人们](https://leetcode.cn/problems/construct-2d-grid-matching-graph-layout/description/)

看点玄学。

随机一道 2400 分，难树形 dp.

答十年月关于同学的玄学问。

mark 一下。

男：壬午 戊申 庚戌 乙酉
女：壬午 己酉 壬午 戊申

父把我昨天自言自语当成语音聊天，难绷，我房间不关门导致的。

写树形 dp，难中难。一开始以为叶子可以不处理，等合并时候再讨论，然后 wa 样例测例 wa 到吐。重新考虑，必须先处理叶子才方便，此后一发过了。计算 `cross` 的容斥部分竟然一开始就没问题。纪念一下目前 lc 里最长 ac 代码，考虑加写加调试三四个小时，梦回一八年初学 cpp 数组模拟约瑟夫环写了大半天被狗女人嘲笑。

[ac](https://leetcode.cn/submissions/detail/577477192/)

贴一下。

```cpp
#include <cmath>
#include <functional>
#include <iostream>
#include <vector>

class LinearSieve {
 public:
  LinearSieve(size_t n) : is_prime_(n + 1, true) {
    is_prime_[0] = false;
    if (n >= 1) {
      is_prime_[1] = false;
    }
    if (n < 2) {
      return;
    }
    primes_.reserve(n / std::log(n));
    for (size_t i = 2; i <= n; i++) {
      if (is_prime_[i]) {
        primes_.emplace_back(i);
      }
      for (size_t j : primes_) {
        if (i * j > n) {
          break;
        }
        is_prime_[i * j] = false;
        if (i % j == 0) {
          break;
        }
      }
    }
  }

  const vector<size_t>& GetPrimes() const { return primes_; }

  const vector<bool>& GetIsPrime() const { return is_prime_; }

 private:
  vector<bool> is_prime_;
  vector<size_t> primes_;
};

using namespace std;

using ll = long long;

class Solution {
 public:
  long long countPaths(int n, vector<vector<int>>& edges) {
    LinearSieve sieve(n);
    const auto& is_prime = sieve.GetIsPrime();

    int root = 1;
    vector<vector<int>> neighbors(n + 1);
    for (auto& edge : edges) {
      neighbors[edge[0]].emplace_back(edge[1]);
      neighbors[edge[1]].emplace_back(edge[0]);
    }

    vector<ll> cross(n + 1), end_prime(n + 1), end_all_comp(n + 1),
        younger(n + 1);
    auto is_leaf = [&](int u) {
      return neighbors[u].size() == 1 && u != root;
    };
    function<void(int, int)> dfs = [&](int u, int fa) {
      if (is_leaf(u)) {
        if (!is_prime[u]) {
          end_all_comp[u] = 1;
        } else {
          end_prime[u] = 1;
        }
        return;
      }
      // younger
      for (auto& son : neighbors[u]) {
        if (son != fa) {
          dfs(son, u);
          younger[u] += cross[son] + younger[son] +
                        (is_prime[son] ? end_prime[son] - 1 : end_prime[son]);
        }
      }
      // end_prime & end_all_comp
      if (is_prime[u]) {
        for (auto& son : neighbors[u]) {
          if (son != fa) {
            end_prime[u] += end_all_comp[son];
          }
        }
        end_prime[u]++;
      } else {
        for (auto& son : neighbors[u]) {
          if (son != fa) {
            end_prime[u] += end_prime[son];
            end_all_comp[u] += end_all_comp[son];
          }
        }
        end_all_comp[u]++;
      }

      // cross
      if (is_prime[u]) {
        ll sum_comp = 0;
        ll sum_self_square = 0;
        for (auto& son : neighbors[u]) {
          if (son != fa) {
            sum_comp += end_all_comp[son];
            sum_self_square += end_all_comp[son] * end_all_comp[son];
          }
        }
        cross[u] = (sum_comp * sum_comp - sum_self_square) / 2;
      } else {
        ll sum_comp = 0;
        ll sum_prime = 0;
        ll sum_combine = 0;
        for (auto& son : neighbors[u]) {
          if (son != fa) {
            sum_comp += end_all_comp[son];
            sum_prime += end_prime[son];
            sum_combine += end_all_comp[son] * end_prime[son];
          }
        }
        cross[u] = sum_comp * sum_prime - sum_combine;
      }
    };

    dfs(root, -1);
    for (int i = 1; i <= n; i++) {
      cout << cross[i] << " " << younger[i] << " " << end_all_comp[i] << " "
           << end_prime[i] << endl;
    }
    return end_prime[root] + younger[root] + cross[root];
  }
};
```

ac 了才看题解，原来只需要维护 `end_prime` 和 `end_all_comp` 就行了，答案可以用一个变量累计。完全是自己想的，就当锻炼脑力和码力了家人们。

插曲，线筛板子 re 了，改写一下操作数写的前半部分。