from de_Bruijn import *
from multiprocessing import Process

min_k = 5  # Set the minimum length of k-mer
max_k = 10  # Set the maximum length of k-mer


def processing(func, data, num):
    """
    Parallelize calculations for fast iteration of the k-mers set
    :param func: function for parallelization
    :param data: set of reads for assembling
    :param num: array of k-mers lengths for each iteration
    """
    p = []
    for task in range(0, len(num)):
        p.append(Process(target=func, args=(data, num[task],)))
    for task in range(0, len(num)):
        p[task].start()
    for task in range(0, len(num)):
        p[task].join()


if __name__ == '__main__':
    from fasta_reader import *
    seq = fasta(choose_file())
    processing(graph, seq, [int(kmer) for kmer in range(min_k, max_k + 1)])
