import yara
import argparse



def main():
    rules = yara.compile(filepath=str(args.rule))
    matches = rules.match(f"{args.binary}")

    if not matches:
        print("No Matches")
        return

    for m in matches:
        print(f"Rule: {m.rule}")
        if hasattr(m,"meta"):
            print("Meta:", m.meta)

        for string_match in m.strings:
            identifier = string_match.identifier  # e.g. $sc1
            for inst in string_match.instances:  # each match instance
                offset = inst.offset
                data = inst.matched_data
                try:
                    s = data.decode("utf-8", errors="replace")
                except Exception:
                    s = repr(data)
                print(f"0x{offset:x}:{identifier}:{s}")
        print()

if __name__ == "__main__":

    
    parser = argparse.ArgumentParser(prog="psiYARA", description="takes yara rules and sample binary to test it against", epilog="\nyara-o-yara");
    parser.add_argument('-r', '--rule', required=True, help="name of rule file, i.e, rules.yar")
    parser.add_argument('-b', '--binary', required=True, help="binary file to test against, ie malware.exe|.out")
    args = parser.parse_args()

    main()

