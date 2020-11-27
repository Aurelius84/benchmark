#   Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from common_import import *


class AbsConfig(APIConfig):
    def __init__(self):
        super(AbsConfig, self).__init__("abs")
        self.feed_spec = {"range": [-1, 1]}
        # abs belongs to activation op series which only has one parameter
        # thus abs can reuse activation.json. 
        self.alias_name = "activation"


class PaddleAbs(PaddleDynamicAPIBenchmarkBase):
    def build_graph(self, config):
        x = self.variable(name="x", shape=config.x_shape, dtype=config.x_dtype)
        self.feed_list = [x]

    def run_graph(self, config):
        result = paddle.abs(x=self.feed_list[0])
        self.fetch_list = [result]
        if config.backward:
            self.append_gradients(result, self.feed_list)


class TorchAbs(PytorchAPIBenchmarkBase):
    def build_graph(self, config):
        x = self.variable(name='x', shape=config.x_shape, dtype=config.x_dtype)
        self.feed_list = [x]

    def run_graph(self, config):
        result = torch.abs(x=self.feed_list[0])
        self.fetch_list = [result]
        if config.backward:
            self.append_gradients(result, self.feed_list)


if __name__ == '__main__':
    test_main(pd_dy_obj=PaddleAbs(), torch_obj=TorchAbs(), config=AbsConfig())