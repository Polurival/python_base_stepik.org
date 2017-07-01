with open('dataset_24465_4.txt', 'r') as f, open('to.txt', 'w') as t:
    t.write('\n'.join(reversed([line.strip() for line in f])))