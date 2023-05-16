import 'dart:math';

void main() {
    List<int> l1 = [3, 4, 7, 9, 8, 5, 1, 2, 5, 7];

    print(l1);

    List<int> l2 = List.generate(10, (index) => Random().nextInt(5) - 5);

    print(l2);

    List<int> lres = [];

    for (int i = 0; i < l1.length; i++) {
        lres.add(l1[i] + l2[i]);
}

    print(lres);

    lres.removeRange(6, 9);

    print(lres);
}