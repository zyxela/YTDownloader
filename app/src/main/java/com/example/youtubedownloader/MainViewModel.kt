package com.example.youtubedownloader

import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel

class MainViewModel : ViewModel() {
    val currentProgress: MutableLiveData<Int> by lazy {
        MutableLiveData<Int>()
    }

    init {
        currentProgress.value = 0
    }



}