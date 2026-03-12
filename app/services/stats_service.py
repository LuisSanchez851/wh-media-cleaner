class StatsService:

    def total_size(self, files):

        return sum(f.size for f in files)

    def count(self, files):

        return len(files)