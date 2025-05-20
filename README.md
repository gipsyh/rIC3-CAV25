# rIC3-CAV25 Artifact

The ```result``` folder contains the evaluated results. Run ```python3 ./utils/main.py``` to analyze the results.

## rIC3
- Compile: See ./rIC3/README.md
- Run:
    - rIC3-ic3: ```cargo r --release -- -e ic3 --ic3-dynamic <AIGER>```
    - rIC3-portfolio: ```cargo r --release -- -e portfolio <AIGER>```

## ABC-Super-Prove
- Download: ```git clone --recursive https://github.com/sterin/super-prove-build.git```
- Requirements: conda
- Compile: Also see ./super-prove-build/README.md
    - ```conda create -y -n py2 python=2.7```
    - ```conda activate py2```
    - ```conda install ninja future -y```
    - ```mkdir super-prove-build/build && cd super-prove-build/build```
    - ```cmake -DCMAKE_BUILD_TYPE=Release -G Ninja   -DCMAKE_LIBRARY_PATH=$CONDA_PREFIX/lib -DPYTHON_LIBRARY=$CONDA_PREFIX/lib/libpython2.7.so -DPYTHON_INCLUDE_DIR=$CONDA_PREFIX/include/python2.7 -DCMAKE_EXE_LINKER_FLAGS="-L$CONDA_PREFIX/lib" ..```
    - ```ninja```
    - ```ninja package```
    - This will create a super_prove-hwmcc20-2-<OS>-Release.tar.gz in the build directory.
- Run:
    - ```tar -zxvf super_prove-hwmcc20-2-<OS>-Release.tar.gz```
    - ```export PYTHONHOME=$CONDA_PREFIX/ && export PYTHONPATH=$CONDA_PREFIX/lib/python2.7/site-packages/ LD_LIBRARY_PATH=$CONDA_PREFIX/lib:$LD_LIBRARY_PATH```
    - ```super_prove/bin/super_prove.sh <AIGER>```


## ABC-pdr
- Compile: See ./abc/README.md
- Run: ```pdr -c "read <AIGER>; logic; undc; strash; zero; pdr -nct"```

## nuXmv
- Run:
    - nuXmv-cav23: See ./nuXmv/README.md

## IC3ref
- Compile:
```
mkdir ./IC3ref/build && cd ./IC3ref/build
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_C_COMPILER=clang -DCMAKE_CXX_COMPILER=clang++ ..
cmake --build . -j
```
- Run: ```./ic3refmain < <AIGER>```

## Avy
- Download: ```git clone https://github.com/TechnionFV/hwmcc24_submission.git Pavy```
- Run:
    - Avy: ```python3 scripts/pavy.py -p kavy3 <AIGER>```
    - Pavy: ```python3 scripts/pavy.py <AIGER>```

## AVR
- Compile: See ./AVR/README.md
- Run:
    - AVR-ic3sa: ```python3 avr.py <BTOR2>```
    - AVR-portfolio: ```python3 avr_pr.py <BTOR2>```

## Pono
- Compile: See ./pono/README.md
- Run:
    - Pono-ic3ia: ```pono -e ic3ia -k 1000000 --pseudo-init-prop <BTOR2>```
    - Pono-ic3sa: ```pono -e ic3sa -k 1000000 --static-coi <BTOR2>```
    - Pono-portfolio: ```python3 ./scripts/parallel_pono.py -k 1000000 <BTOR2>```
