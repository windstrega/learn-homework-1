"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

sold_phones = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
product_sum_list = []

for product_dict in sold_phones:
  items_sold = product_dict['items_sold']
  product = product_dict['product']

  sold_sum = sum(items_sold)
  product_sum_list.append(sold_sum)

  print(f'Суммарное количество продаж товара {product}: {sold_sum}')

all_sum = sum(product_sum_list)
print(f'Суммарное количество продаж всех товаров {all_sum}')

def count_item_avg(items_sold):
  sold_sum = 0
  for sold in items_sold:
    sold_sum += sold
    sold_avg = sold_sum / len(items_sold)
    return sold_sum

total_sold_avg_sum = 0
for one_item in sold_phones:
  item_avg = count_item_avg(one_item['items_sold'])
  print(f'Среднее количество продаж товара {one_item["product"]}: {item_avg}')
  total_sold_avg_sum += item_avg

print(f'Среднее количество продаж всех товаров: {total_sold_avg_sum / len(sold_phones)}')
    
    
if __name__ == "__main__":
    main()
