import subprocess


def md_to_rst(filename):
    try:
        out = subprocess.check_output('pandoc -t rst -i {}'.format(filename), shell=True)
    except subprocess.CalledProcessError:
        # pandoc is probably not installed
        return 'README: https://github.com/jarhill0/hnpy#hnpy'
    return out.decode('utf-8')  # bytes to str
