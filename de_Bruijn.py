def graph(data, k):
    """
    Build De Bruijn graph
    :param data: set of reads for assembling
    :param k: num of kmer
    :return: print assembling genomes and their length for each of kmers lengths
    """
    bruijn = {}  # graph
    last_edge = []  # array of the last kmers, which helps to understand whether a sequence is circular or linear
    lines = []  # array
    # normalize of reads
    for line in range(len(data)):
        data[line] = data[line].upper()
    # add edges and nodes from each reads to dict, the last kmer from each string has not k+1 mer now (_)
    for line in data:
        for nuc in range(len(line) - k):
            bruijn[line[nuc:nuc + k]] = line[nuc:nuc + k + 1]
        bruijn[line[len(line) - k:len(line)]] = '_'
    # add k+1 mer for each last kmer (with _) from other reads, where it is possible
    for node in bruijn:
        if bruijn.get(node) == '_':
            for edge in bruijn:
                if node[1:] == edge[:-1]:
                    bruijn.update({node: node[0] + edge})
            if bruijn.get(node) == '_':
                last_edge.append(node)
    # assembling genome for the circular sequence
    if not last_edge:
        ans = data[-1][-k:]
        for _ in bruijn:
            ans += bruijn.get(ans[-k:])[-1]
    # assembling genome for the linear sequence
    else:
        l_l = 0  # number of answers for each kmers length
        # assembling genome from each edge
        for edge in bruijn:
            ans = edge
            # assemble while it is being assembled
            for _ in range(len(bruijn)):
                if ans[-k:] in bruijn:
                    ans += bruijn.get(ans[-k:])[-1]
                else:
                    break
            # quick checking for a substring (in the same read), because we need only the longest (start edge)
            c = 0
            for line in lines:
                if ans in line:
                    c += 1
                    break
            if c == 0:
                lines.append(ans[:-1])
            # checking for a substring (in different reads), because we need only the longest (start edge)
            if len(lines) > l_l:
                rm_set = set()
                for elem in lines:
                    for ot_elem in lines:
                        if elem != ot_elem:
                            if ot_elem in elem:
                                rm_set.add(ot_elem)
                for el in rm_set:
                    lines.remove(el)
                l_l = len(lines)
        # sorting and control check
        ans = sorted(lines, key=len, reverse=True)
        rm_set = set()
        for elem in ans:
            for ot_elem in ans:
                if elem != ot_elem:
                    if ot_elem in elem:
                        rm_set.add(ot_elem)
        for el in rm_set:
            ans.remove(el)
    # printing the assembling sequences and their lengths for each kmers lengths
    if type(ans) is str:
        print('\nLength of kmer:', k, '\nLength of sequence:', len(ans), '\nSequence:', ans)
    else:
        for line in ans:
            print('\nLength of kmer:', k, '\nLength of sequence:', len(line), '\nSequence:', line)
