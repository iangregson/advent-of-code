from pathlib import Path

# file = Path(__file__).parent / "test_input.txt"
file = Path(__file__).parent / "input.txt"
lines = file.read_text().splitlines()

class Moon:
    def __init__(self, *, p = (0,0,0), v = (0,0,0), name = 'Moon') -> None:
        self.p = p
        self.v = v
        self.name = name

    def __repr__(self) -> str:
        return f"{self.name}(pos={self.p}, vel={self.v})"

    @staticmethod
    def from_str(s: str, *, name: str = 'Moon'):
        s = s[1:-1]
        x, y, z = [int(k.replace(',','')[2:]) for k in s.split(' ')]
        return Moon(p=(x, y, z), name=name)

    @property
    def energy(self):
        potential = sum([abs(x) for x in self.p])
        kinetic = sum([abs(x) for x in self.v])
        return potential * kinetic

class Simulator():
    def __init__(self, moons: dict[Moon] = {}) -> None:
        self.moons = moons
        self.T = 0

    def __repr__(self) -> str:
        return "\n".join([str(moon) for moon in self.moons.values()])

    def add_moon(self, moon: Moon):
        self.moons[moon.name] = moon

    def step(self):
        # apply gravity to update velocities
        # apply velocities to update positions
        # print(f'\nAfter {self.T} steps:')
        # print(self)
        self.apply_gravity()
        self.apply_velocity()
        self.T += 1

    @property
    def moon_pairs(self) -> list[tuple[str]]:
        moon_pairs = []
        moons = list(sorted(self.moons.keys()))
        n = len(moons)
        for i in range(n):
            for j in range(n):
                if j == i:
                    continue
                pair = (moons[i], moons[j])
                moon_pairs.append(pair)

        return list(set([tuple(pair) for pair in map(sorted, moon_pairs)]))


    def apply_gravity(self):
        for pair in self.moon_pairs:
            a, b = pair

            ax, ay, az = self.moons[a].p
            bx, by, bz = self.moons[b].p

            avx, avy, avz = self.moons[a].v
            bvx, bvy, bvz = self.moons[b].v

            # x
            if bx > ax:
                avx += 1
                bvx -= 1
            elif ax > bx:
                bvx += 1
                avx -= 1

            # y
            if by > ay:
                avy += 1
                bvy -= 1
            elif ay > by:
                bvy += 1
                avy -= 1

            # z
            if bz > az:
                avz += 1
                bvz -= 1
            elif az > bz:
                bvz += 1
                avz -= 1
            
            self.moons[a].v = (avx, avy, avz)
            self.moons[b].v = (bvx, bvy, bvz)


    def apply_velocity(self):
        for moon in self.moons:
            x, y, z = self.moons[moon].p
            vx, vy, vz = self.moons[moon].v
            x += vx
            y += vy
            z += vz
            self.moons[moon].p = (x,y,z)

    @property
    def total_energy(self):
        return sum([moon.energy for moon in self.moons.values()])


S = Simulator()

for idx, moon_name in enumerate(['Io', 'Europa', 'Ganymede', 'Callisto']):
    moon = Moon.from_str(lines[idx], name=moon_name)
    S.add_moon(moon)


for step in range(1000):
    S.step()

print(S.total_energy)