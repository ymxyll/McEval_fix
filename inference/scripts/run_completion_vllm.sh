
MODEL_DIR='<model_dir>'

COMPLETE_DATA_PATH='../../python_eval_data/completion/merge'

OUT_DIR='../../out/wait_to_split'


python ../inference_vllm.py \
    --data_path $COMPLETE_DATA_PATH \
    --base_model $MODEL_DIR \
    --task 'completion'  \
    --outdir $OUT_DIR


COMPLETE_DATA_PATH='../../python_eval_data/completion/light'
python ../inference_vllm.py \
    --data_path $COMPLETE_DATA_PATH \
    --base_model $MODEL_DIR \
    --task 'completion_light'  \
    --outdir $OUT_DIR

