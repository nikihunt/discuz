# -*- coding: utf-8 -*-


class A(object):

    def __init__(self):
        super(A, self).__init__()
        print "A!"


class B(object):

    def __init__(self):
        super(B, self).__init__()
        print "B!"


class AB(A, B):

    def __init__(self):
        super(AB, self).__init__()
        print "AB!"


# class C(object):

#     def __init__(self):
#         super(C,  self).__init__()
#         print "C!"


# class D(object):

#     def __init__(self):
#         super(D, self).__init__()
#         print "D!"


# class CD(C, D):

#     def __init__(self):
#         super(CD, self).__init__()
#         print "CD!"


# class ABCD(AB, CD):

#     def __init__(self):
#         super(ABCD, self).__init__()
#         print "ABCD!"


def main():
    obj = AB()

if __name__ == '__main__':
    main()
