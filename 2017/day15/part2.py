epoch = 5000000
divisor = 2147483647
factorA = 16807
multipleA = 4
factorB = 48271
multipleB = 8
A = 277
B = 349

import queue

qA = queue.Queue(maxsize=epoch)
qB = queue.Queue(maxsize=epoch)

while not qA.full():
    A = (A * factorA) % divisor
    if A % multipleA == 0:
        qA.put(A)

while not qB.full():
    B = (B * factorB) % divisor
    if B % multipleB == 0:
        qB.put(B)

def next(qA, qB, epoch):
    i = 0
    while i < epoch:
        A = qA.get()
        B = qB.get()
        yield [A, B]
        i += 1

count_matches = 0

for [A, B] in next(qA, qB, epoch):
    binaryA = bin(A)[-16:]
    binaryB = bin(B)[-16:]
    print(binaryA, binaryB)
    if binaryA == binaryB:
        count_matches += 1

print(count_matches)
