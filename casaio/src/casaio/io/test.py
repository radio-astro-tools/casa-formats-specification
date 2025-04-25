from casaio.io import table

def run():
    t = table.Table(basename="/home/mystletainn/Development/casaio/data/Antennae_North.cal.lsrk.ms")
    data = t.get_column(name="DATA")


if __name__ == "__main__":
    run()