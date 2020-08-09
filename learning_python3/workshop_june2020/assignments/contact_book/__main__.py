from contactbook.cmdline import get_parser

args = get_parser().parse_args()
args.handler_func(args)
