import re
import operator

CONST_SOURCE_STRING = "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudant" \
                      "ium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beata" \
                      "e vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odi" \
                      "t aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. N" \
                      "eque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, " \
                      "sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat vo" \
                      "luptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit labor" \
                      "iosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui i" \
                      "n ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat " \
                      "quo voluptas nulla pariatur?"

# Пункт 1: Все слова без знаков препинания. Используем обычную регулярку
re_trimmed = re.findall('[A-z]+', CONST_SOURCE_STRING)
print(re_trimmed)

# Пункт 2: слово и количество его появлений:
d_grouped = {}
for i in re_trimmed:
    if d_grouped.get(i) is None:
        d_grouped[i] = CONST_SOURCE_STRING.count(i)
print(d_grouped)

# Пункт 3: TOP-10 самых встречающихся слов. Решение со StackOverflow
i = 0
for k in sorted(d_grouped.items(), key=operator.itemgetter(1), reverse=True):
    if i >= 10:
        break
    print(k)
    i += 1
