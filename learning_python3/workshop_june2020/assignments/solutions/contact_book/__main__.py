import logging

from contactbook.cmdline import get_parser

logging.basicConfig(
    level=logging.DEBUG, format="[%(asctime)s][%(levelname)s][%(name)s] %(message)s"
)

logger = logging.getLogger(__name__)

args = get_parser().parse_args()
logging.debug(f"Arguments = {args}")
args.handler_func(args)
