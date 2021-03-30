from datam import Tileset

CollatzTileset = Tileset()
CollatzTileset.temperature = 2
CollatzTileset.add_glue("bin.0", 1)
CollatzTileset.add_glue("bin.1", 1)
CollatzTileset.add_glue("ter.0", 1)
CollatzTileset.add_glue("ter.1", 1)
CollatzTileset.add_glue("ter.2", 1)

CollatzTileset.add_tile_type("0", ["bin.0", "ter.0", "bin.0", "ter.0"])
CollatzTileset.add_tile_type("1", ["bin.0", "ter.1", "bin.1", "ter.0"])
CollatzTileset.add_tile_type("2", ["bin.0", "ter.2", "bin.0", "ter.1"])
CollatzTileset.add_tile_type("3", ["bin.1", "ter.0", "bin.1", "ter.1"])
CollatzTileset.add_tile_type("4", ["bin.1", "ter.1", "bin.0", "ter.2"])
CollatzTileset.add_tile_type("5", ["bin.1", "ter.2", "bin.1", "ter.2"])

DamienTileset = Tileset()
DamienTileset.temperature = 2
DamienTileset.add_glue("bin.0", 1)
DamienTileset.add_glue("bin.1", 1)

DamienTileset.add_tile_type("A", ["bin.0", "bin.0", "bin.1", None])
DamienTileset.add_tile_type("B", ["bin.0", "bin.1", "bin.1", "bin.0"])
DamienTileset.add_tile_type("C", ["bin.1", "bin.0", "bin.1", "bin.0"])
DamienTileset.add_tile_type("D", ["bin.1", "bin.1", "bin.0", "bin.1"])