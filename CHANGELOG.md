# Changelog

## 0.1.0 (2026-05-13)

Full Changelog: [v0.0.1...v0.1.0](https://github.com/battements-falaises/court-listener-sdk-python/compare/v0.0.1...v0.1.0)

### Features

* **internal/types:** support eagerly validating pydantic iterators ([7c342ea](https://github.com/battements-falaises/court-listener-sdk-python/commit/7c342eaf3aa5028e02cdb0e5515f5bd3b39709ec))
* **internal:** implement indices array format for query and form serialization ([79549fa](https://github.com/battements-falaises/court-listener-sdk-python/commit/79549fac30dd08b2fb5050e360ac6554d9b47e8c))
* support setting headers via env ([160c67d](https://github.com/battements-falaises/court-listener-sdk-python/commit/160c67da9136c30f1c6bd7e6c335d96d5d5a9536))


### Bug Fixes

* **client:** add missing f-string prefix in file type error message ([e2c110d](https://github.com/battements-falaises/court-listener-sdk-python/commit/e2c110d9d0e5fe6f288add0835aabcb77b61fff8))
* **client:** preserve hardcoded query params when merging with user params ([ee793cc](https://github.com/battements-falaises/court-listener-sdk-python/commit/ee793ccf9511e5f48a5719c9c8009ef4259c71e1))
* **deps:** bump minimum typing-extensions version ([f32ed09](https://github.com/battements-falaises/court-listener-sdk-python/commit/f32ed09992bf86815d23784d56241eebb7d9ecb8))
* ensure file data are only sent as 1 parameter ([ded77f8](https://github.com/battements-falaises/court-listener-sdk-python/commit/ded77f819a9c5f1f018c0c456257b31b8d4b1bda))
* **pydantic:** do not pass `by_alias` unless set ([e4c3d48](https://github.com/battements-falaises/court-listener-sdk-python/commit/e4c3d48ae37a38c6937e304fcacf0719fb1545da))
* sanitize endpoint path params ([fef950f](https://github.com/battements-falaises/court-listener-sdk-python/commit/fef950f96ce19534e80f766ea4d38f61b42073b7))
* use correct field name format for multipart file arrays ([de078da](https://github.com/battements-falaises/court-listener-sdk-python/commit/de078daec2f06e931a2aea63abca1c35a6f85fd5))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([af16fda](https://github.com/battements-falaises/court-listener-sdk-python/commit/af16fda78564689d55e2c296657c4217e5f2d2e2))


### Chores

* **ci:** skip lint on metadata-only changes ([601b211](https://github.com/battements-falaises/court-listener-sdk-python/commit/601b21177eb4141677f183f5b8666299c1cd78fa))
* **ci:** skip uploading artifacts on stainless-internal branches ([82c4bb3](https://github.com/battements-falaises/court-listener-sdk-python/commit/82c4bb3d11066ef84702291b6de295f6ec8ad5cf))
* configure new SDK language ([e951ff7](https://github.com/battements-falaises/court-listener-sdk-python/commit/e951ff7a4bb6e4407c8d76e9f3580ed4c1040e5f))
* configure new SDK language ([e99802d](https://github.com/battements-falaises/court-listener-sdk-python/commit/e99802d582e97ee412a8343ccd5d02ac0b407b45))
* configure new SDK language ([f0e3029](https://github.com/battements-falaises/court-listener-sdk-python/commit/f0e3029a690e05e563d869d1f84b26c4366259bc))
* **internal:** codegen related update ([a923ec4](https://github.com/battements-falaises/court-listener-sdk-python/commit/a923ec4ca1b06f0ff68f0199aaba438746f8e47c))
* **internal:** more robust bootstrap script ([45f2851](https://github.com/battements-falaises/court-listener-sdk-python/commit/45f2851dd99781ca478bee4cd94575ec0e978d3d))
* **internal:** refactor authentication internals ([c0f3ebc](https://github.com/battements-falaises/court-listener-sdk-python/commit/c0f3ebc097792259c4b8316161cf9b5913af4a69))
* **internal:** reformat pyproject.toml ([4e9f93c](https://github.com/battements-falaises/court-listener-sdk-python/commit/4e9f93c4dd10d3044eceb28a992a18985ec05b29))
* **internal:** tweak CI branches ([82a558d](https://github.com/battements-falaises/court-listener-sdk-python/commit/82a558d114cd39911d6e13582465adc0fc4a63d6))
* **internal:** update gitignore ([27d173f](https://github.com/battements-falaises/court-listener-sdk-python/commit/27d173fcc63768bf7d64f3da7e34504c6dc00138))
* **test:** do not count install time for mock server timeout ([99166c2](https://github.com/battements-falaises/court-listener-sdk-python/commit/99166c21a26eec6660f8d2f6150d220e50e8be92))
* **tests:** bump steady to v0.19.4 ([fac60bd](https://github.com/battements-falaises/court-listener-sdk-python/commit/fac60bd44802dccb64cf20b7da39d4cf82e659b3))
* **tests:** bump steady to v0.19.5 ([fe6c603](https://github.com/battements-falaises/court-listener-sdk-python/commit/fe6c603d8fb1f9cfbfb89c836e6da2d3014500c3))
* **tests:** bump steady to v0.19.6 ([8eadf0e](https://github.com/battements-falaises/court-listener-sdk-python/commit/8eadf0e8f462205384d363261c60e84d206bc0d7))
* **tests:** bump steady to v0.19.7 ([afb5c74](https://github.com/battements-falaises/court-listener-sdk-python/commit/afb5c744b939a529bc0d43d3859bc6c93ab3bde4))
* **tests:** bump steady to v0.20.1 ([e50b4e3](https://github.com/battements-falaises/court-listener-sdk-python/commit/e50b4e3b62820c51c631e763564a93bb3a623a1a))
* **tests:** bump steady to v0.20.2 ([2993a84](https://github.com/battements-falaises/court-listener-sdk-python/commit/2993a84b468281e7df1d3e8e7b838f57a99055d7))
* **tests:** bump steady to v0.22.1 ([9c2ed01](https://github.com/battements-falaises/court-listener-sdk-python/commit/9c2ed0117a0261cb56c35fc457960bfc02815947))
* **tests:** change mock server to steady ([35c5df5](https://github.com/battements-falaises/court-listener-sdk-python/commit/35c5df5db82897c54492043f6f724af2c4f1b63f))
* update SDK settings ([53a0cfb](https://github.com/battements-falaises/court-listener-sdk-python/commit/53a0cfbbe3850a18df34cfc228c8e3b305e289d5))
* update SDK settings ([2ef21ba](https://github.com/battements-falaises/court-listener-sdk-python/commit/2ef21ba19a14dbcfb878910b2faf1bdbe6b0f6ed))
