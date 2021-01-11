
import getopt, sys



def caesar(data, key, mode):
  pass
  alphabet='abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWYZ'
  new_data = ''
  for c in data:
    index = alphabet.find(c)
    if index == -1:
      new_data += c
    else:
      new_index = index + key if mode == 1 else index - key
      new_index %= len(alphabet)
      new_data += alphabet[new_index:new_index+1]
  return new_data


key = 5
original = 'the quick brown fox jumps over the lazy dog'
print('Original:', original)
ciphered = caesar(original, key, 1)
print('  Cipher:', ciphered)



plain = caesar(ciphered, key, 0)
print('   Plain:', plain)





if __name__ == '__main__':
    syntax = 'k:m:i:o:'
    # Default arguments
    key = 1
    mode = 1
    out_file = 'out.txt'
    in_file = 'in.txt'
    try:
        opts, args = getopt.getopt(sys.argv[1:], syntax)
        for o, a in opts:
            if o == '-k':
                key = int(a)
            elif o == '-m':
                mode = int(a)
            elif o == '-i':
                in_file = a
            elif o == '-o':
                out_file = a

        # Read file
        with open(in_file, 'rt') as f:
            data = f.read()
        # Translate it
        new_data = caesar(data, key, mode)
        with open(out_file, 'wt') as f:
            f.write(new_data)

    except getopt.GetoptError as err:
        print('Error parsing args:', err)
        sys.exit(1)
    except Exception as e:
        print('Error', e)
        sys.exit(2)