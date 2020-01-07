from dmoj.result import CheckerResult

def check(process_output, judge_output, judge_input, point_value, execution_time, **kwargs):
  process_output = process_output.decode("utf-8").split("\n")[:-1]
  judge_input = judge_input.decode("utf-8").split("\n")
  n, m = (int(x) for x in judge_input[0].split())
  lhs = [int(x) for x in judge_input[1].split()]
  rhs = [int(x) for x in judge_input[2].split()]
  try:
    p = int(process_output[0])
    assert len(process_output) == p+1
    assert 1 <= p <= 1000000
    for triple in process_output[1:]:
      u, v, w = (int(x) for x in triple.split())
      assert 1 <= u <= n
      assert 1 <= v <= m
      u -= 1
      v -= 1
      assert w <= lhs[u]
      assert w <= rhs[v]
      lhs[u] -= w
      rhs[v] -= w
    assert sum(lhs) == 0
    assert sum(rhs) == 0
  except Exception as e:
    return CheckerResult(False, 0, "{}".format(e))
  return True
