class Computer:
    def __init__(self, cpu, ram, gpu, storage):
        self.cpu = cpu
        self.ram = ram
        self.gpu = gpu
        self.storage = storage

class ComputerBuilder:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.gpu = None
        self.storage = None

    def set_cpu(self, cpu):
        self.cpu = cpu
        return self

    def set_ram(self, ram):
        self.ram = ram
        return self

    def set_gpu(self, gpu):
        self.gpu = gpu
        return self

    def set_storage(self, storage):
        self.storage = storage
        return self

    def build(self):
        return Computer(self.cpu, self.ram, self.gpu, self.storage)

# Client code
builder = ComputerBuilder()
computer = builder.set_cpu("Intel i7").set_ram("16GB").set_gpu("Nvidia RTX 3080").set_storage("1TB SSD").build()
