def main():
  LIST = []
  VALUE = input('Enter a value: ')
  LIST.append(VALUE)

  while VALUE:
    VALUE = input('Enter a value: ')
    if VALUE != '':
      LIST.append(VALUE)
  print(LIST)


if __name__ == "__main__":
    main()
