def hannuota(n, x, y, z):
	if n == 1:
		print(x, " --> ", z)
	else:
		# 将前 n-1 个盘子从x移动到y上
		hannuota(n-1, x, z, y)

		#将最底下的最后一个盘子从x 移动到 z上
		print(x, " --> ", z)

		#将前 n-1 个盘子从 y 移动到 z 上
		hannuota(n-1, y, x, z)

n = int(input("请输入汉诺塔的层数："))
hannuota(n, "X", "Y", "Z")