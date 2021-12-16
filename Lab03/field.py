# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items, *args):
    assert len(args) > 0
    if len(args)==1:
        for item in items:
            result = item.get(args[0])
            print(result)
    else:
        for item in items:
            result = {key: item.get(key) for key in args if item.get(key) is not None}
            print(result)

def main():
    goods = [{'title': 'Ковер', 'price': 2000, 'color': 'green'},
             {'title': 'Диван для отдыха', 'color': 'black'}
             ]


    field(goods, 'title')

    field(goods, 'title', 'price')

if __name__ == "__main__":
    main()
