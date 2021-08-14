import os, sys
import ROOT as root
from optparse import OptionParser

parser = OptionParser()
parser.add_option('-e', '--expectSignal', help='expectSignal', dest='expectSignal', default='1')
parser.add_option('-m', '--minimizer', help='minimizer', dest='cminDefaultMinimizerType', default='Minuit')


(options, args) = parser.parse_args()
#print(options)
additional_args = []
additional_args.append("--ignoreCovWarning")
additional_args.append("--saveShapes")
additional_args.append("--saveWithUncertainties")
additional_args.append("--saveWorkspace")
additional_args.append("--plots")
additional_args.append("--forceRecreateNLL")
#additional_args.append("")
#additional_args.append("")

def build_and_run_command(file_fullPath, options_dict, additional_args, *args):
    assert os.path.exists(file_fullPath)
    basic_cmd = "combine -M FitDiagnostics -d "+file_fullPath
    print(type(basic_cmd))
    basic_cmd += " --expectSignal "+ options_dict.expectSignal
    basic_cmd += " --cminDefaultMinimizerType "+options_dict.cminDefaultMinimizerType
    
        

    if "fast" in args:
        if "--saveShapes" in additional_args:
            additional_args.remove("--saveShapes")
        if "--saveWorkspace" in additional_args:
            additional_args.remove("--saveWorkspace")
        if "--plots" in additional_args:
            additional_args.remove("--plots")

    if "robust" in args:
        additional_args.append("--robustFit=1")

    for additional_arg in additional_args:
        basic_cmd += " "+additional_arg

    
    print("**** Running the following Command ===>>>>")
    print(basic_cmd)
    os.system(basic_cmd)



combined_datacards = []
combined_datacards.append("/eos/uscms/store/user/abhd1994/darkhiggs_type1_nobtag_nostat_uncs/datacards/Mz500mhs70Mdm500/Mz500mhs70Mdm500.txt")



build_and_run_command(combined_datacards[0], options, additional_args, "fast")
