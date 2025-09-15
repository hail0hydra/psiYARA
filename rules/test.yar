rule testing_hex
{
    meta:
        author = "hail0hydra"
        description = "to test if a file is ELF or EXE(PE)"

    strings:
        $hex1 = { 7F 45 4C 46 } // for ELF
        $hex2 = { 4D 5A } // PE

    condition:
        $hex1 or $hex2
}
