# Copyright 2023 The KerasNLP Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from tools.sentencepiece_testing.utils import _save
from tools.sentencepiece_testing.utils import _train_sentencepiece


def main():
    bytes_io = _train_sentencepiece(
        ["the quick brown fox", "the earth is round"],
        vocab_size=11,
        model_type="WORD",
        bos_id=-1,
        pad_id=0,
        eos_id=1,
        unk_id=2,
        pad_piece="<pad>",
        eos_piece="</s>",
        unk_piece="<unk>",
        user_defined_symbols="[MASK]",
    )
    _save(bytes_io, "t5_sentencepiece.proto")

    bytes_io = _train_sentencepiece(
        ["abc"],
        vocab_size=5,
        pad_id=-1,
        eos_id=-1,
        bos_id=-1,
    )
    _save(bytes_io, "t5_sentencepiece_bad.proto")


if __name__ == "__main__":
    main()