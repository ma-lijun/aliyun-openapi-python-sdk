# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class UpdateIntentRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Chatbot', '2017-10-11', 'UpdateIntent','beebot')

	def get_IntentDefinition(self):
		return self.get_body_params().get('IntentDefinition')

	def set_IntentDefinition(self,IntentDefinition):
		self.add_body_params('IntentDefinition', IntentDefinition)

	def get_IntentId(self):
		return self.get_query_params().get('IntentId')

	def set_IntentId(self,IntentId):
		self.add_query_param('IntentId',IntentId)