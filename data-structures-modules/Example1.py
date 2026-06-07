from collections import Counter

if __name__ == '__main__':
    """
        Getting Started With Counter Module
    """
    names_list = ['Mark','Johnny','David','Mark','Johnny','Mark','James','Mathew']

    c = Counter(names_list)
    print(c)

    print(c['Mark'])

    print(c.get('Mark'))

    keys =  c.keys()
    print(keys)

    values = c.values();
    print(values)

    c.update({'Ajay':4})

    for ele in c.elements():
        print(ele,end=" ")

    c.pop("Ajay")

    print("\nAfter removing Ajay")

    for ele in c.elements():
        print(ele, end=" ")

    m_common_names =  c.most_common(1)
    print(f"\n{m_common_names}")

    m_common_names =  c.most_common(2)
    print(f"{m_common_names}")