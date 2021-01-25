class Combine:

    def sides(self, sides):
        combined = ''
        for face in 'URFDLB':
            combined += ''.join(sides[face])
        return combined


combine = Combine()
