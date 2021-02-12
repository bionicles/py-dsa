test:
	pytest

env-created:
	conda create -q -y -n py39 python=3.9

env-active: env-created
	conda activate py39

