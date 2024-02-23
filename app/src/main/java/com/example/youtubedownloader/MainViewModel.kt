package com.example.youtubedownloader

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.chaquo.python.PyObject
import kotlinx.coroutines.Job
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.launch

class MainViewModel : ViewModel() {

    val currentProgress = MutableStateFlow<Int>(0)
var p = 0
  
    private var job: Job? = null

    fun updateProgress(module: PyObject) {
        job = viewModelScope.launch {
            Thread {
                while (true) {
                    val status = module.callAttr("r")
                    val value = status.toInt()
                    currentProgress.value = value
                    p = value
                }
            }.start()
        }

    }


    fun startVideoDownloading(module: PyObject, link: String) {
        viewModelScope.launch {
            module.callAttr("start", link, "video")
        }
    }

    fun startAudioDownloading(module: PyObject, link: String) {
        viewModelScope.launch {
            module.callAttr("start", link, "audio")
        }
    }

    fun cancelProgress() {
        job?.cancel()
    }
}
