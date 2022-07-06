import argparse


# Argument
parser = argparse.ArgumentParser()
parser.add_argument('--list_data', type=int, nargs='+')
args = parser.parse_args()


print('Results:', args.list_data)