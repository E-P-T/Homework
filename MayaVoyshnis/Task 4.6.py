def get_longest(s):
    print(max(s.replace('\t',' ').replace('\n',' ').split(' '),key=len))
if __name__ == '__main__':
    get_longest('Any pythonista like namespaces a lot.')