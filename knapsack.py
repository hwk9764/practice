import timeit


class best_combi():
    def __init__(self, names, values, weights):
        self.names = names
        self.values = values
        self.weights = weights
        self.opt_names = []  # 모든 경우의 수_물건 이름
        self.opt_value = 0  # 모든 경우의 수_물건의 가치
        self.opt_weight = 0  # 모든 경우의 수_물건의 무게

    def find_best_combi(self, capacity):  # 이진법으로 모든 경우의 수 따져 최대 가치 찾아내는 함수
        start = timeit.default_timer()
        for case in range(1, 2 ** len(self.names)):  # i => 모든 경우의 수
            sum_value = 0  # 조건을 만족하는 조합 가치들의 총합
            sum_weight = 0  # 조건을 만족하는 조합 무게들의 총합
            for bit in range(len(self.names)):  # j => 비교할 비트 수
                if (case & 2 ** bit) == 2 ** bit:  # 이진수 각 자리와 경우의 수를 비교하여 조건에 맞는 조합들을 리스트에 저장할 것
                    # 굳이 이진수로 변환할 필요 없이 십진수 숫자로 연산해도 이진수 연산한 것과 같은 결과 출력
                    sum_weight += self.weights[bit]
                    sum_value += self.values[bit]

            if (sum_value > self.opt_value and sum_weight <= capacity) or (
                    sum_value == self.opt_value and sum_weight < self.opt_weight):
                # 이전에 계산한 조합의 가치보다 크고, 용량보다 무게가 적거나 / 이전에 계산한 조합의 가치와 같은데 이전에 계산한 조합의 무게보단 적을 때
                self.opt_value = sum_value
                self.opt_weight = sum_weight
                name_index = case
                
        for i in range(len(self.names)):
            if (name_index & 2 ** i) == 2 ** i:
                self.opt_names.append(self.names[i])

        print('최대 가치는', self.opt_value,
              '이고 그 때의 조합은', self.opt_names,
              '이며 그 조합의 총 무게는', self.opt_weight, '이다')
        end = timeit.default_timer()
        print('time :', end - start)
        return 0


names = ['a', 'b', 'c', 'd', 'e']  # 물건의 이름
values = [10, 30, 20, 14, 23]  # 물건의 값어치
weights = [5, 8, 3, 7, 9]  # 물건의 무게
capacity = 20  # 가방의 용량

a = best_combi(names, values, weights)
a.find_best_combi(capacity)
