.venv/bin/python run_directly.py \
    /home/xuananh/work/viralize/viralize \
    --target-function direct_vast::DirectVAST.get  \
    --downstream-depth=3 \
    --exclude-namespaces=kpi_optimizer,rate_limiters_update \
    --language=py \
    --output=direct_vast_get.png

.venv/bin/python -m debugpy --listen localhost:5678 --wait-for-client run_directly.py \
    /home/xuananh/work/viralize/viralize \
    --target-function direct_vast::DirectVAST.get  \
    --downstream-depth=3 \
    --exclude-namespaces=kpi_optimizer,rate_limiters_update \
    --language=py \
    --output=direct_vast_get.png


.venv/bin/python run_directly.py \
    example/callable_class_instance/callable_class_instance.py \
    --output example/callable_class_instance/result.png \
    --language py
    
.venv/bin/python -m debugpy --listen localhost:5678 --wait-for-client run_directly.py \
    example/callable_class_instance/callable_class_instance.py \
    --output example/callable_class_instance/result.png \
    --language py


.venv/bin/python run_directly.py \
    /home/xuananh/work/viralize/viralize \
    --target-function svast::SVAST.get  \
    --downstream-depth=3 \
    --exclude-namespaces=kpi_optimizer,rate_limiters_update \
    --language=py \
    --output=svast_get.png


.venv/bin/python -m debugpy --listen localhost:5678 --wait-for-client run_directly.py \
    /home/xuananh/work/viralize/viralize \
    --target-function svast::SVAST.get  \
    --downstream-depth=3 \
    --exclude-namespaces=kpi_optimizer,rate_limiters_update \
    --language=py \
    --output=svast_get.png


.venv/bin/python run_directly.py \
    /home/xuananh/repo/code2flow/code2flow/engine.py \
    /home/xuananh/repo/code2flow/code2flow/model.py \
    /home/xuananh/repo/code2flow/code2flow/python.py \
    --target-function engine::map_it \
    --downstream-depth=10 \
    --output result1.png \
    --language py