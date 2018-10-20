class Udacian():
    def __init__(self, name, city, nanodegree, enrollment, status):
        self.name = name
        self.city = city
        self.nanodegree = nanodegree
        enroll = enrollment.split(' ')
        self.enrollment = enroll[0] + ' (' + enroll[len(enroll)-1] + ')'
        self.status = status

    def print_udacian(self):
        print('{} is enrolled in {} studying {}, with Ms. {}, he/she is {}'.format(self.name, self.city, self.nanodegree, self.enrollment, self.status))


udi = Udacian('Ali', 'Khobar', 'FSND', 'Elham AM', 'Ontrack')
udi.print_udacian()