from subject_area.detail import Detail
from subject_area.provider import Provider
from subject_area.details_prov import DetailsProv

from operator import itemgetter

providers = [
    Provider(1, "Vista", "Russia"),
    Provider(2, "KROS", "Ukraine"),
    Provider(3, "SKUBA", "Litva"),
]

details = [
    Detail(1, "nut", "copper", 1),
    Detail(2, "washer", "lead", 2),
    Detail(3, "screw", "aluminum", 3),
    Detail(4, "lens", "glass", 3)
]


details_prov = [
    DetailsProv(1, 1),
    DetailsProv(1, 2),

    DetailsProv(2, 2),
    DetailsProv(2, 3),

    DetailsProv(3, 3),
    DetailsProv(3, 1),

    DetailsProv(4, 3),
    DetailsProv(4, 2)
]

def main():

    one_to_many = [(det.name, prov.name, prov.country)
                   for det in details
                   for prov in providers
                   if det.prov_id == prov.id
                   ]

    many_to_many_temp = [(prov.name, dp.prov_id, dp.detail_id)
                         for prov in providers
                         for dp in details_prov
                         if prov.id == dp.prov_id]

    many_to_many = [(det.name, prov_name)
                    for prov_name, prov_id, detail_id in many_to_many_temp
                    for det in details if det.id == detail_id]

    print('\nЗадание Б1')
    task_1 = sorted(one_to_many, key=itemgetter(0))
    print(task_1)


    print('\nЗадание Б2')
    task_2 = []
    for prov in providers:
        det_prov = list(filter(lambda elem: elem[1] == prov.name, one_to_many))
        task_2.append([prov.name, len(det_prov)])
    print(sorted(task_2, key=itemgetter(1)))


    print('\nЗадание Б3')
    task_3 = {}
    for det in details:
        if (det.name.startswith('n') or det.name.startswith('l')):
            det_prov = list(
                filter(lambda elem: elem[0] == det.name, many_to_many))
            task_3[det.name] = [x for _, x in det_prov]
    print(task_3)

if __name__ == "__main__":
    main()