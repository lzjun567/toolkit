1. 请求方法get、post最终是被tornado httpserver调用的，那么调用请求方法（get、post）时，参数一定也是由httpserver提供。
2. 那么httpserver从哪里获取请求方法说需要的参数呢？分析源代码
            
            #web.py 1364行
            #这里是真正调用请求方法的代码
            def _execute_method(self):
                if not self._finished:
                    method = getattr(self, self.request.method.lower())
                    print('method:', method)
                    print('args:', self.path_args)
                    print('kwargs:', self.path_kwargs)
                    tmp = method(*self.path_args, **self.path_kwargs)  #重点看这行
                    print (tmp)
                    self._when_complete(tmp,
                                        self._execute_finish)
                                        
3. 关键字参数是通过self.path_kwargs传递过去的，那么它的值是怎么生成的呢？继续跟踪代码：  
            
            #1325  RequestHandler
            def _execute(self, transforms, *args, **kwargs):
                """Executes this request with the given output transforms."""
                self._transforms = transforms
                try:
                    if self.request.method not in self.SUPPORTED_METHODS:
                        raise HTTPError(405)
                    self.path_args = [self.decode_argument(arg) for arg in args]
                    self.path_kwargs = dict((k, self.decode_argument(v, name=k)) #在这行赋的值
                                            for (k, v) in kwargs.items())
                                            
            
            #1829 Application
            def __call__():
                '''省略很多行'''
             handler._execute(transforms, *args, **kwargs)
             
            
            #1802 Application
            def __call__():
            '''省略....'''
             if spec.regex.groupindex:
                            kwargs = dict(    #这个是真正的关键字参数的初始化
                                (str(k), unquote(v))
                                for (k, v) in match.groupdict().items())
                        else:
                            args = [unquote(s) for s in match.groups()]

4. spec是URLSpec(第2679行)实例对象，    self.regex = re.compile(pattern)  #2698
                                 
 regex.groupindex：如果正则表达式中定义了(?P<id>)带名字的分组的话，那么regex.groupindex返回的是{id:position}构成的字典。

https://docs.python.org/3.5/library/re.html